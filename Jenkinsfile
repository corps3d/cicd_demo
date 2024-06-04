pipeline {
    agent any

    environment {
        AZURE_CREDENTIALS = credentials('azuresp')
        AZURE_SUBSCRIPTION_ID = '3839b40f-e660-4e3d-a81f-1bc7d6f50fc1'
        AZURE_RESOURCE_GROUP = 'cicd_pipeline'
        AZURE_FUNCTION_APP = 'hellocorpsed'
    }

    stages {
        stage('Pull Code') {
            steps {
                git branch: 'main', url: 'https://github.com/corps3d/cicd_demo'
            }
        }

        stage('Build Project') {
            steps {
                sh 'python -m venv venv'
                sh 'source venv/bin/activate'
                sh 'pip install -r requirements.txt'
            }
        }

        stage('Run Tests') {
            steps {
                sh 'source venv/bin/activate'
                sh 'pytest'
            }
        }

        stage('Package Application') {
            steps {
                sh 'zip -r functionapp.zip *'
                archiveArtifacts artifacts: 'functionapp.zip', allowEmptyArchive: true
            }
        }

        stage('Deploy Application') {
            steps {
                withCredentials([azureServicePrincipal(credentialsId: 'azuresp')]) {
                    sh '''
                    az login --service-principal -u $AZURE_CREDENTIALS_USR -p $AZURE_CREDENTIALS_PSW --tenant $AZURE_CREDENTIALS_TENANT
                    az account set --subscription $AZURE_SUBSCRIPTION_ID

                    az functionapp deployment source config-zip \
                        --resource-group $AZURE_RESOURCE_GROUP \
                        --name $AZURE_FUNCTION_APP \
                        --src functionapp.zip
                    '''
                }
            }
        }
    }

    post {
        always {
            cleanWs()
        }
    }
}
