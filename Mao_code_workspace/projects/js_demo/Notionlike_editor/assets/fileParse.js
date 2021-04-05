/**
 * 读取文件
 * 
 * 
 * <input type="file" id="files" style="display: none" onchange="fileImport();">
 * <input type="button" id="fileImport" value="导入">
 *
 * //点击导入按钮,使files触发点击事件,然后完成读取文件的操作
        $("#fileImport").click(function(e) {
            $("#files").click();
            $("#files").val("");
            e.preventDefault();
        });
 */
function readFile() {
    var selectedFile = document.getElementById('files').files[0];
    alert(selectedFile);
    var reader = new FileReader(); //这是核心,读取操作就是由它完成.
    reader.readAsText(selectedFile); //读取文件的内容,也可以读取文件的URL
    reader.onload = function() {
        //当读取完成后回调这个函数,然后此时文件的内容存储到了result中,直接操作即可
        // console.log(this.result);
        let json = JSON.parse(this.result);
        window.fileJsonData = this.result;
    };
}

/**
 * 保存json格式的文件=================会自动下载
 * 
 * <input type="button" id="export" value="保存"/
 * <script src="https://cdn.bootcss.com/FileSaver.js/1.3.8/FileSaver.js"></script>
 * var button = document.getElementById("export");
button.addEventListener("click", saveHandler, false);
 */
function downFile1(data, name) {
    var content = JSON.stringify(data, null, 4);
    var blob = new Blob([content], {
        type: "text/plain;charset=utf-8"
    });
    saveAs(blob, name);
}
/**
 * 自动下载json文件===============不依赖
 * @param {json数据} jsondata 
 * @param {文件名字} name 
 */
function downFile2(jsondata, name) {
    var output = JSON.stringify(jsondata, null, 4);
    console.log(output[Blocks]);
    var el = document.createElement('a');
    el.setAttribute('href', 'data:text/plain;charset=utf-8,' + output);
    el.setAttribute('download', './' + name);
    el.style.display = 'none';
    document.body.appendChild(el);
    el.click();
    document.body.removeChild(el);
}