pipeline {
    agent any
    
    stages {
        stage('Clone Repository') {
            steps {
                // Clone the repository
                sh 'git clone --depth 1 https://github.com/Meenakshi0812/zip-application.git'
            }
        }
        
        stage('Deploy to Apache') {
            steps {
                // Generate folder name based on timestamp
                script {
                    def folderName = sh(script: 'date +"%Y%m%d%H%M%S"', returnStdout: true).trim()
                
                    // Move app.py to /var/www/html/<folderName>
                    sh "sudo mv zip-application/app.py /var/www/html/${folderName}"
                }
            }
        }
        
        stage('Create Soft Link') {
            steps {
                // Create soft link for the deployed code
                sh "sudo ln -s /var/www/html/${folderName} /var/www/html/current"
            }
        }
    }
}
