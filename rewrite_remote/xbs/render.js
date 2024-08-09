/*
 * @Author: bgcode
 * @Date: 2024-08-05 12:51:41
 * @LastEditors: bgcode
 * @LastEditTime: 2024-08-09 13:15:45
 * @Description: 
 * @FilePath: /QX/rewrite_remote/xbs/render.js
 */
const url = "https://cdn.jsdelivr.net/gh/bgvioletsky/QX@0.0.7/rewrite_remote/xbs/render.html";
const myRequest = {
    url: url
};

$task.fetch(myRequest).then(response => {
    $done({bodyBytes: response.bodyBytes});
}, reason => {
    $done();
});