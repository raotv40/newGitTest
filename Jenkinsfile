pipeline { 

    agent any 

  

    environment { 

        REPO_URL   = 'https://github.com/raotv40/newGitTest.git' 

        BRANCH     = 'master'            // change to 'main' if your repo uses that 

        SCRIPT_NAME = 'langchaindemo/script_test50.py' 

        // Keep double backslashes for Windows paths 

        PYTHON_PATH = 'C:\\\\Users\\\\dell\\\\AppData\\\\Local\\\\Programs\\\\Python\\\\Python312\\\\python.exe' 

        // If your repo is private, set CREDENTIALS_ID to your Jenkins credential id 

        CREDENTIALS_ID = '' // e.g. 'github-ssh' or 'github-token', leave empty for public repo 

    } 

  

    stages { 

        stage("Checkout Code") { 

            steps { 

                echo "Checking out ${REPO_URL}@${BRANCH}" 

                script { 

                    if (env.CREDENTIALS_ID) { 

                        git branch: "${BRANCH}", 

                            url: "${REPO_URL}", 

                            credentialsId: "${CREDENTIALS_ID}" 

                    } else { 

                        git branch: "${BRANCH}", 

                            url: "${REPO_URL}" 

                    } 

                } 

                // List workspace files to confirm script exists 

                script { 

                    if (isUnix()) { 

                        sh 'ls -la' 

                    } else { 

                        bat 'dir' 

                    } 

                } 

            } 

        } 

  

        stage('Validate Python Installation') { 

            steps { 

                script { 

                    if (isUnix()) { 

                        // prefer explicit python3 if available 

                        sh 'which python3 || which python || echo "no python binary found on PATH"' 

                        sh 'python3 --version || python --version || true' 

                    } else { 

                        // quote both executable and filename 

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

                            // Use python3 if available, else python 

                            sh 'python3 ${SCRIPT_NAME} || python ${SCRIPT_NAME}' 

                        } else { 

                            // Quote both the python path and the script (handles spaces) 

                            bat "\"${PYTHON_PATH}\" \"${SCRIPT_NAME}\"" 

                        } 

                    } catch (Exception e) { 

                        // include the pipeline log for debugging 

                        error("Failed to execute Python script: ${e.getMessage()}") 

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