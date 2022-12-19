pipeline {
            options {timestamps()}

            environment {
                registry = "mxrem/prog-tech-exam-app-pipeline"
                registryCredential = 'maxrem-dockerhub'
                dockerImage = ''
            }

            agent none
            stages {
                stage('Check scm') {
                    agent any
                    steps {
                      checkout scm
                    }
                }// stage Build
                stage('Build') {
                    steps {
                      echo "Building ...${BUILD_NUMBER}"
                      echo "Build completed"
                    }
                }// stage Build
                stage('Test') {
                    agent { docker { image 'alpine'
                              args '-u=\"root\"'
                            }
                        }
                    steps {
                      sh 'apk add --update python3 py-pip'
                      sh 'pip install xmlrunner'
                      sh 'python3 app_test.py'
                    }
                    post {
                        always {
                           //  junit 'test-reports/*.xml'
									junit allowEmptyResults: true, testResults: '**/test-results/*.xml'
                            }
                        success {
                            echo "Application testing successfully completed "
                        }
                        failure {
                            echo "Oooppss!!! Tests failed!"
                        } // post
                    } 
                } // stage Test
                stage('Image building') {
                    steps {
                        script {
                            dockerImage = docker.build registry + ":$BUILD_NUMBER"
                        }
                    }
                }
                stage('Delivery') {
                    steps {
                        script {
                            docker.withRegistry( '', registryCredential ) {
                                dockerImage.push()
                            }
                        }
                    }
                }
            } // stages
}