def call(String jsonPath = 'trivy-report.json', String outputPath = 'trivy-report.html') {
    def report = readJSON file: jsonPath

    def html = """
        <html><head>
        <style>
        body { font-family: Arial; }
        .HIGH, .CRITICAL { color: red; font-weight: bold; }
        .MEDIUM { color: orange; }
        .LOW { color: green; }
        .UNKNOWN { color: gray; }
        </style>
        </head><body>
        <h2>🛡️ Trivy Vulnerability Report</h2>
    """

    report.each { image ->
        html += "<h3>🔍 ${image.Target}</h3><ul>"
        image.Vulnerabilities.each { vuln ->
            def sev = vuln.Severity
            html += "<li class='${sev}'>[${sev}] <b>${vuln.VulnerabilityID}</b> in ${vuln.PkgName} \
                     - Fix: ${vuln.FixedVersion ?: 'N/A'} \
                     <a href='${vuln.References?.getAt(0) ?: "#"}'>📖</a></li>"
        }
        html += "</ul>"
    }

    html += "</body></html>"
    writeFile file: outputPath, text: html
}
