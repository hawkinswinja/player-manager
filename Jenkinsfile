pipeline {
    agent {
        label 'pm-prod'
    }

    parameters {
        choice(choices:['update','deploy'], description: 'fkf build Choice', name: 'CHOICE')
    }
    stages {
        stage ('Build') {
            steps {
                sh 'make build'
            }
        }
        
        stage ('Test') {
            steps {
                sh 'make test'
            }
        }
        
        stage('Push') {
            environment {
                DOCKER = credentials('docker')
            }
	        steps {
                sh 'TAG=${env.BUILD_ID} DOCKER_USERNAME=${DOCKER_USR} DOCKER_PASSWORD=${DOCKER_PSW} make push'
            }
        }

        stage('Deploy') {
            when { 
                expression { env.CHOICE == 'deploy' }
            }
	        environment {
                FKF_ADMIN = credentials('fkf-admin')
                ALLOWED_HOSTS = credentials('allowed-hosts')
            }
            steps {
                sh 'TAG=${env.BUILD_ID} DEBUG=0 SECRET_KEY=${FKF_ADMIN_PSW} ALLOWED_HOSTS=${ALLOWED_HOSTS} FKF_ADMIN=${FKF_ADMIN_USR} FKF_PASSWORD=${FKF_ADMIN_PSW} make new_deploy'
            }
        }

        stage('Update') {
            when { 
                    expression { env.CHOICE == 'update' }
            }
            environment {
                FKF_ADMIN = credentials('fkf-admin')
                ALLOWED_HOSTS = credentials('allowed-hosts')
            }
            steps {
                    sh 'TAG=${env.BUILD_ID} DEBUG=0 SECRET_KEY=${FKF_ADMIN_PSW} ALLOWED_HOSTS=${ALLOWED_HOSTS} FKF_ADMIN=${FKF_ADMIN_USR} FKF_PASSWORD=${FKF_ADMIN_PSW} make update'
            }
        }
    }

    post {
        failure {
            echo 'notify job status as failure'
        }
        success {
            echo 'notify job status as success'
        }
        always {
            deleteDir() /* clean up our workspace */
            echo 'One way or another, I have finished'
        }
    }
}
