pipeline {
    agent any
    
    stages {
        stage('Clone Repository') {
            steps {
                script {
                    def timeStamp = new Date().format("yyyy-MM-dd-HH:mm:ss")
                    sh "git clone https://github.com/Meenakshi0812/zip-application.git ${timeStamp}.zip"
                }
            }
        }
        
        stage('Copy and Unzip') {
            steps {
                script {
                    def timeStamp = new Date().format("yyyy-MM-dd-HH:mm:ss")
                    sh "cp ${timeStamp}.zip /var/www/html/"
                    dir("/var/www/html/") {
                        sh "unzip ${timeStamp}.zip"
                    }
                }
            }
        }
        
        stage('Deploy to Apache') {
            steps {
                script {
                    def timeStamp = new Date().format("yyyy-MM-dd-HH:mm:ss")
                    sh "ln -s /var/www/html/${timeStamp} /var/www/html/latest"
                    sh "rm /var/www/html/index.html" // Remove existing index.html if present
                    sh "cp /var/www/html/${timeStamp}/index.html /var/www/html/index.html" // Copy the repository's index.html to /var/www/html/
                    // Additional Apache configuration can be added here if necessary
                }
            }
        }
    }
}
