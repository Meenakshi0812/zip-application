pipeline {
    agent any
    
    stages {
        stage('Clone Repository') {
            steps {
                script {
                    def timeStamp = new Date().format('yyyyMMddHHmmss')
                    sh "git clone https://github.com/Meenakshi0812/zip-application.git ${timeStamp}.zip"
                }
            }
        }
        
        stage('Copy and Unzip') {
            steps {
                script {
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
                    sh "ln -s /var/www/html/${timeStamp} /var/www/html/latest"
                    // Additional Apache configuration can be added here if necessary
                }
            }
        }
    }
}
