/*
 * @Author: bgcode
 * @Date: 2024-08-05 12:51:41
 * @LastEditors: bgcode
 * @LastEditTime: 2024-08-23 18:29:57
 * @Description: 
 * @FilePath: /QX/rewrite_remote/xbs/render.js
 */
const url = "http://192.168.1.6:8080/render.html";
const myRequest = {
    url: url
};

$task.fetch(myRequest).then(response => {
    $done({bodyBytes: response.bodyBytes});
}, reason => {
    $done();
});