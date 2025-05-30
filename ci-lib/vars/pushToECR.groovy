// vars/pushToECR.groovy
/**
 * Push Docker image to AWS ECR.
 *
 * @param config Map with keys:
 *   - region     : AWS region (e.g., us-east-1)
 *   - accountId  : AWS account ID
 *   - image      : Fully qualified Docker image name with tag
 */
def call(Map config = [:]) {
    def region    = config.region ?: error("Missing region")
    def accountId = config.accountId ?: error("Missing accountId")
    def image     = config.image ?: error("Missing image name")

    def ecrUrl = "${accountId}.dkr.ecr.${region}.amazonaws.com"

    steps.echo "Logging in to AWS ECR..."
    steps.sh """
        aws ecr get-login-password --region ${region} | \
        docker login --username AWS --password-stdin ${ecrUrl}
    """

    steps.echo "Pushing image to ECR: ${image}"
    steps.sh "docker push ${image}"

    steps.echo "Image pushed to ECR successfully."
}
