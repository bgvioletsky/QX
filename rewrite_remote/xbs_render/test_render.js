/*
 * @Author: bgcode
 * @Date: 2024-08-05 12:51:41
 * @LastEditors: bgcode
 * @LastEditTime: 2024-08-09 12:49:04
 * @Description: 
 * @FilePath: /QX/rewrite_remote/xbs_render/test_render.js
 */
const url = "https://raw.githubusercontent.com/bgvioletsky/QX/main/rewrite_remote/xbs_render/test.html";
const myRequest = {
    url: url
};

$task.fetch(myRequest).then(response => {
    $done({bodyBytes: response.bodyBytes});
}, reason => {
    $done();
});