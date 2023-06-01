pipeline {
    agent any
    
    stages {
        stage('Clone Repository') {
            steps {
                script {
                    def timeStamp = new Date().format("yyyy-MM-dd-HH-mm-ss")
                    sh "git clone https://github.com/Meenakshi0812/zip-application.git ${timeStamp}.zip"
                }
            }
        }
        
        stage('Copy and Unzip') {
            steps {
                script {
                    def timeStamp = new Date().format("yyyy-MM-dd-HH-mm-ss")
                    def folderName = "/var/www/html/${timeStamp}"
                    
                    sh "cp ${WORKSPACE}/${timeStamp}.zip ${folderName}.zip"
                    dir("/var/www/html/") {
                        sh "unzip ${folderName}.zip"
                    }
                }
            }
        }
        
        stage('Deploy to Apache') {
            steps {
                script {
                    def timeStamp = new Date().format("yyyy-MM-dd-HH-mm-ss")
                    def folderName = "/var/www/html/${timeStamp}"
                    
                    sh "ln -s ${folderName} /var/www/html/latest"
                    sh "rm /var/www/html/index.html" // Remove existing index.html if present
                    sh "cp ${folderName}/index.html /var/www/html/index.html" // Copy the repository's index.html to /var/www/html/
                    // Additional Apache configuration can be added here if necessary
                }
            }
        }
    }
}
