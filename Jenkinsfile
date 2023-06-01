pipeline {
    agent any

    stages {
        stage('Clone Repository') {
            steps {
                script {
                    def timeStamp = new Date().format("yyyy-MM-dd-HH-mm-ss")
                    def folderName = timeStamp
                    sh "git clone https://github.com/Meenakshi0812/zip-application.git ${folderName}"
                }
            }
        }

        stage('Copy and Unzip') {
            steps {
                script {
                    def timeStamp = new Date().format("yyyy-MM-dd-HH-mm-ss")
                    def folderName = timeStamp
                    def sourcePath = "${folderName}/${folderName}.zip"
                    def destinationPath = "/var/www/html/${folderName}/"

                    sh "cp ${sourcePath} ${destinationPath}"
                    dir(destinationPath) {
                        sh "unzip ${folderName}.zip"
                        sh "rm ${folderName}.zip"
                    }
                }
            }
        }

        stage('Deploy to Apache') {
            steps {
                script {
                    def timeStamp = new Date().format("yyyy-MM-dd-HH-mm-ss")
                    def folderName = timeStamp
                    def sourcePath = "/var/www/html/${folderName}"
                    def destinationPath = "/var/www/html/latest"
                    def indexFilePath = "/var/www/html/index.html"

                    sh "ln -s ${sourcePath} ${destinationPath}"
                    sh "rm ${indexFilePath}" // Remove existing index.html if present
                    sh "cp ${sourcePath}/index.html ${indexFilePath}" // Copy the repository's index.html to /var/www/html/
                    // Additional Apache configuration can be added here if necessary
                }
            }
        }
    }
}
