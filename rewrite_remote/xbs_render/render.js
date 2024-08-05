/*
 * @Author: bgcode
 * @Date: 2024-08-05 12:51:41
 * @LastEditors: bgcode
 * @LastEditTime: 2024-08-05 22:47:14
 * @Description: 
 * @FilePath: /QX/rewrite_remote/xbs_render/render.js
 */
const url = "https://raw.githubusercontent.com/bgvioletsky/QX@0.0.2/main/rewrite_remote/xbs_render/render.html";
const myRequest = {
    url: url
};

$task.fetch(myRequest).then(response => {
    $done({bodyBytes: response.bodyBytes});
}, reason => {
    $done();
});