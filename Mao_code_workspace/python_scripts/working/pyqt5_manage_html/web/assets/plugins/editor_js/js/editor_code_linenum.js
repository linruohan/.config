// JS给Textarea文本框添加行号的方法
// 本文实例讲述了JS给Textarea文本框添加行号的方法。分享给大家供大家参考。具体如下：
//
// 这里使用JS实现让Textarea文本框显示行号的功能，每一行的前面都会有下数字序号，
// 如果用来显示代码的话，可以直接找到某一行，
// 如果不显示行号，则还要自己手功去查，想要此功能，你只需设置好TextArea ID，
// 并加入代码中的JavaScript代码部分即可，文本框的长宽则是由CSS来控制的，
// 你可试着修改一下，长宽的显示要与JS相匹配。
/*
 <style type="text/css">
 #codeTextarea{width: 500px;height: 310px;}
.textAreaWithLines{font-family: courier;border: 1px solid #ddd;}
.textAreaWithLines textarea,.textAreaWithLines div{border: 0px;line-height: 120%;font-size: 12px;}
.lineObj{color: #666;}
</style>
//使用：
<form>
<textarea id="codeTextarea"></textarea>
</form>
<script type="text/javascript">
createTextAreaWithLines('codeTextarea');
</script>
*
* */
















let lineObjOffsetTop = 2;

function createTextAreaWithLines(className) {
    let el = document.createElement('DIV');
    let ta = document.getElementsByClassName(className);
    ta.parentNode.insertBefore(el, ta);
    el.appendChild(ta);
    el.className = 'textAreaWithLines';
    el.style.width = (ta.offsetWidth + 30) + 'px';
    ta.style.position = 'absolute';
    ta.style.left = '30px';
    el.style.height = (ta.offsetHeight + 2) + 'px';
    el.style.overflow = 'hidden';
    el.style.position = 'relative';
    el.style.width = (ta.offsetWidth + 30) + 'px';
    let lineObj = document.createElement('DIV');
    lineObj.style.position = 'absolute';
    lineObj.style.top = lineObjOffsetTop + 'px';
    lineObj.style.left = '0px';
    lineObj.style.width = '27px';
    el.insertBefore(lineObj, ta);
    lineObj.style.textAlign = 'right';
    lineObj.className = 'lineObj';
    var string = '';
    for (var no = 1; no < 20; no++) {
        if (string.length > 0) string = string + '<br>';
        string = string + no;
    }
    ta.onkeydown = function () {
        positionLineObj(lineObj, ta);
    };
    ta.onmousedown = function () {
        positionLineObj(lineObj, ta);
    };
    ta.onscroll = function () {
        positionLineObj(lineObj, ta);
    };
    ta.onblur = function () {
        positionLineObj(lineObj, ta);
    };
    ta.onfocus = function () {
        positionLineObj(lineObj, ta);
    };
    ta.onmouseover = function () {
        positionLineObj(lineObj, ta);
    };
    lineObj.innerHTML = string;
}

function positionLineObj(obj, ta) {
    obj.style.top = (ta.scrollTop * -1 + lineObjOffsetTop) + 'px';
}


