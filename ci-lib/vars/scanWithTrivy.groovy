def call() {
    echo '🔍 Running Trivy scan...'
    sh '''
        if ! command -v trivy > /dev/null; then
            echo "Trivy not installed. Skipping scan."
            exit 1
        fi

        IMAGE_NAME="orders"
        docker build -t $IMAGE_NAME .
        trivy image --severity HIGH,CRITICAL $IMAGE_NAME
    '''
}
