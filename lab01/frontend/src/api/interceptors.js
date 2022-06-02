import { TODO_API } from "./todo/http-common";
import { AUTH_API } from "./auth/http-common";


export default function setup(){
    // Add a request interceptor
    TODO_API.interceptors.request.use(function (config) {
        config['headers']['Authorization'] = 'Bearer ' + sessionStorage.getItem('jwt')
        return config;
    }, function (error) {
        // Do something with request error
        return Promise.reject(error);
    });

    // Add a request interceptor
    AUTH_API.interceptors.request.use(function (config) {
        if (config.url != '/api/v1/users/register/'){
            config['headers']['Authorization'] = 'Bearer ' + sessionStorage.getItem('jwt')
        }       
        return config;
    }, function (error) {
        // Do something with request error
        return Promise.reject(error);
    });
}