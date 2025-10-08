pipeline {
    agent any
    
    environment {
        REPO_URL = 'https://github.com/raotv40/newGitTest.git'
        BRANCH = 'master'
        SCRIPT_NAME = 'script_test1.py'
        PYTHON_PATH = 'C:\\Users\\dell\\AppData\\Local\\Programs\\Python\\Python312\\python.exe'
    }
    
    stages {
        stage("Checkout Code") {
            steps {
                echo "Checking out code from ${REPO_URL}"
                git branch: "${BRANCH}", 
                    url: "${REPO_URL}"
            }            
        }
        
        stage('Validate Python Installation') {
            steps {
                script {
                    if (isUnix()) {
                        sh 'python --version'
                    } else {
                        bat "\"${PYTHON_PATH}\" --version"
                    }
                }
            }
        }
        
        stage('Run Python Script') {
            steps {
                script {
                    echo "Running Python script: ${SCRIPT_NAME}"
                    try {
                        if (isUnix()) {
                            sh "python ${SCRIPT_NAME}"
                        } else {
                            bat "\"${PYTHON_PATH}\" ${SCRIPT_NAME}"
                        }
                    } catch (Exception e) {
                        error("Failed to execute Python script: ${e.message}")
                    }
                }
            }
        }
    }
    
    post {
        success {
            echo '✅ Pipeline completed successfully!'
        }
        failure {
            echo '❌ Pipeline failed!'
        }
        always {
            echo 'Pipeline execution finished'
        }
    }
}
