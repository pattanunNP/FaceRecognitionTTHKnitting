# FaceRecognitionTTHKnitting

[![Python 3.8.x](https://img.shields.io/badge/python-3.8-green.svg)](https://www.python.org/downloads/release/python-360/)

# Table of Content

* [Table of contents](#table-of-contents)

* [Quick start](#quick-start)

* [RabbitMQ](#rabbit-mq)

* [About Redis](#about-redis)


## About Redis

Redis is key&value based in-memmory database which used in queue system of this project. we use redis for store processed result. example result JSON below.

```json
{
    task-id:"06a68cec-d7c2-4718-99cd-caca0516ed37",
    status:"SUCCESS",
    task-type:"face-search",
    input-file:"xxx.jpg",
    input-size:"2.4MB",
    input-width:"200px",
    input-hight:"400px",
    argorithm:"spotify",
    feature-size:512,
    modelpath:"model.index",
    result:{
        n-faces:5,
        k-match:2,
        faces:{
            0:{
                face-location:{
                    x:122,
                    y:22,
                    w:24,
                    h:22
                }
                match:{
                    0:{
                        name:"arm",
                        prob:"0.23",
                        path:"runner/r01-arm"
                    },
                    1:{
                        name:"pop",
                        prob:"0.33",
                        path:"runner/r02-pop"
                    }
                }
            },
            1:{ face-location:{
                    x:122,
                    y:22,
                    w:24,
                    h:22
                }
                match:{
                    0:{
                        name:"arm",
                        prob:"0.23",
                        path:"runner/r01-arm"
                    },
                    1:{
                        name:"pop",
                        prob:"0.33",
                        path:"runner/r02-pop"
                    }
                }},
            2:{ face-location:{
                    x:192,
                    y:22,
                    w:27,
                    h:22
                }
                match:{
                    0:{
                        name:"arm",
                        prob:"0.23",
                        path:"runner/r01-arm"
                    },
                    1:{
                        name:"pop",
                        prob:"0.33",
                        path:"runner/r02-pop"
                    }
                }},
            3:{ face-location:{
                    x:122,
                    y:22,
                    w:24,
                    h:22
                }
                match:{
                    0:{
                        name:"arm",
                        prob:"0.23",
                        path:"runner/r01-arm"
                    },
                    1:{
                        name:"pop",
                        prob:"0.33",
                        path:"runner/r02-pop"
                    }
                }},
            4:{ face-location:{
                    x:122,
                    y:22,
                    w:24,
                    h:22
                }
                match:{
                    0:{
                        name:"arm",
                        prob:"0.23",
                        path:"runner/r01-arm"
                    },
                    1:{
                        name:"pop",
                        prob:"0.33",
                        path:"runner/r02-pop"
                    }
                }
            },

        }
        
    }
}

```