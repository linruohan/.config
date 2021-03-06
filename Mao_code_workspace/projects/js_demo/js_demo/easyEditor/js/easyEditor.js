;
(function() {
    "use strict"
    if ((typeof Range !== "undefined") && !Range.prototype.createContextualFragment) { Range.prototype.createContextualFragment = function(html) { var frag = document.createDocumentFragment(),
                div = document.createElement("div");
            frag.appendChild(div);
            div.outerHTML = html; return frag; }; }
    var ieVersion = (function() { var userAgent = navigator.userAgent; var isIE = userAgent.indexOf("compatible") > -1 && userAgent.indexOf("MSIE") > -1; var isEdge = userAgent.indexOf("Edge") > -1 && !isIE; var isIE11 = userAgent.indexOf('Trident') > -1 && userAgent.indexOf("rv:11.0") > -1; if (isIE) { var reIE = new RegExp("MSIE (\\d+\\.\\d+);");
            reIE.test(userAgent); var fIEVersion = parseFloat(RegExp["$1"]); if (fIEVersion == 7) { return 7; } else if (fIEVersion == 8) { return 8; } else if (fIEVersion == 9) { return 9; } else if (fIEVersion == 10) { return 10; } else { return 6; } } else if (isEdge) { return 'edge'; } else if (isIE11) { return 11; } else { return -1; } })();
    var isFirefox = navigator.userAgent.indexOf('Firefox') >= 0;
    var isChrome = navigator.userAgent.indexOf('Chrome') >= 0;
    var defaultContent;
    var defaultOhterContent;
    if (ieVersion === 9 || ieVersion === 10) { defaultContent = '<p></p>';
        defaultOhterContent = '<p>&nbsp;</p>'; } else { defaultContent = '<p><br></p>';
        defaultOhterContent = ''; }
    setTimeout(function() {
        var styleList = { '.easyEditor': ['text-align: left', 'overflow-y: auto', 'word-break: break-all', 'word-wrap: break-word', ], '.easyEditor img': ['cursor: default', 'resize: none', 'vertical-align: middle', '-ms-user-select:none', ], '.easyEditor[contentEditable=true]:not(:focus):before': ['color:#aaa', 'content:attr(placeholder)', ] };
        var styleHtml = '';
        for (var i in styleList) {
            styleHtml += i + '{'
            for (var j = 0; j < styleList[i].length; j++) { styleHtml += styleList[i][j] + ';' }
            styleHtml += '}'
        }
        var docStyle = document.getElementById('easyEditor-style');
        if (docStyle == null) { var style = document.createElement('style');
            style.id = 'easyEditor-style';
            style.type = 'text/css';
            style.innerHTML = styleHtml;
            document.getElementsByTagName('head')[0].appendChild(style);
            style = null; } else { docStyle.innerHTML = styleHtml; }
    }, 1);
    var removeEvent = function(_ele, eType, bol) { if (!_ele.editEvent) return false; var handleType = eType.split('.')[0]; var handleName = eType.split('.')[1] || 'all'; if (!_ele.editEvent[handleName + handleType]) return false; var handle = _ele.editEvent[handleName + handleType]; if (_ele.addEventListener) { bol = bol == undefined ? false : bol;
            _ele.removeEventListener(handleType, handle, bol); } else if (_ele.attachEvent) { _ele.detachEvent("on" + handleType, handle); } else { _ele["on" + handleType] = null; } }
    var addEvent = function(_ele, eType, handle, bol) {
        if (!_ele.editEvent) { _ele.editEvent = new Object; }
        var handleType = eType.split('.')[0];
        var handleName = eType.split('.')[1] || 'all';
        if (!handleType) return false;
        if (_ele.editEvent[handleName + handleType] != undefined) { removeEvent(_ele, eType); }
        _ele.editEvent[handleName + handleType] = handle;
        if (_ele.addEventListener) { bol = bol == undefined ? false : bol;
            _ele.addEventListener(handleType, handle, bol); } else if (_ele.attachEvent) { _ele.attachEvent("on" + handleType, handle); } else { _ele["on" + handleType] = handle; }
    }
    var addClass = function(_ele, className) { var oldClass = _ele.getAttribute('class'); var classList = (_ele.getAttribute('class') || '').split(' ');
        classList.push(className);
        _ele.setAttribute('class', classList.join(' ')); }
    var getRect = function(_ele) { var rect = _ele.getBoundingClientRect(); var _left = document.documentElement.clientLeft; var _top = document.documentElement.clientTop; return { left: rect.left - _left, top: rect.top - _top, right: rect.right - _left, bottom: rect.bottom - _top, width: rect.right - rect.left, height: rect.bottom - rect.top } }
    var removeElement = function(_ele) { var _parentElement = _ele.parentNode; if (_parentElement) { _parentElement.removeChild(_ele); } }
    var insertAfter = function(newEl, targetEl) { var parentEl = targetEl.parentNode; if (parentEl.lastChild == targetEl) { parentEl.appendChild(newEl); } else { parentEl.insertBefore(newEl, targetEl.nextSibling); } }
    var userSelection;
    if (window.getSelection) { userSelection = window.getSelection(); } else if (document.selection) { userSelection = document.selection.createRange(); }
    var getRangeObject = function() {
        var rangeObject;
        rangeObject = userSelection;
        if (userSelection.getRangeAt) { rangeObject = userSelection.getRangeAt(0); }
        return rangeObject;
    }
    var setRange = function(range) { if (window.getSelection) { userSelection.removeAllRanges();
            userSelection.addRange(range); } else if (document.selection) { range.select(); } }
    var filter = function() {
        var _ele = this.editbox;
        try { document.execCommand("AutoUrlDetect", false, false); } catch (e) {}
        addEvent(_ele, 'paste.filter', function(event) {
            var event = event || window.event;
            if (event.preventDefault) { event.preventDefault(); } else { event.returnValue = false; }
            var textRange;
            var text = null;
            if (window.clipboardData && clipboardData.setData) { text = window.clipboardData.getData('text'); } else { text = (event.originalEvent || event).clipboardData.getData('text/plain'); }
            if (document.body.createTextRange) {
                if (document.selection) { textRange = document.selection.createRange(); } else if (window.getSelection) { var sel = window.getSelection(); var range = sel.getRangeAt(0); var tempEl = document.createElement("span");
                    tempEl.innerHTML = "";
                    range.deleteContents();
                    range.insertNode(tempEl);
                    textRange = document.body.createTextRange();
                    textRange.moveToElementText(tempEl);
                    tempEl.parentNode.removeChild(tempEl); }
                textRange.text = text;
                textRange.collapse(false);
                textRange.select();
            } else { document.execCommand("insertText", false, text); }
        });
    }
    var restoreContent = function(editbox) { var html = editbox.innerHTML; if (html.length === 0 || html === '<br>') { editbox.innerHTML = defaultContent; } }
    var checkPlaceholder = function() { var editbox = this.editbox; if (this.placeholderContent && this.placeholderText != '') { var html = editbox.innerHTML; if (html === defaultContent || html === defaultOhterContent) { editbox.setAttribute('placeholder', this.placeholderText); } else { editbox.removeAttribute('placeholder'); } } else if (!this.placeholderContent) { editbox.removeAttribute('placeholder'); } }
    var bindEvent = function() {
        var _this = this;
        addEvent(_this.editbox, 'click.edit', function(event) { setTimeout(function() { _this.saveRange(); }, 1); });
        addEvent(_this.editbox, 'keypress.edit', function() { _this.saveRange(); });
        addEvent(_this.editbox, 'keyup.edit', function(event) { _this.saveRange(); var event = event || window.event; if (event.keyCode === 8) { restoreContent(_this.editbox); } });
        addEvent(_this.editbox, 'blur.edit', function() { checkPlaceholder.call(_this); })
        _this.editbox.dragOnEdit = false;
        addEvent(_this.editbox, 'dragstart.edit', function(event) { _this.editbox.dragOnEdit = true; });
        addEvent(_this.editbox, 'dragend.edit', function(event) { _this.editbox.dragOnEdit = false; });
        addEvent(_this.editbox, 'drop.edit', function(event) { if (_this.editbox.dragOnEdit) { setTimeout(function() { _this.saveRange(); }, 1);
                _this.editbox.dragOnEdit = false; } else { var event = event || window.event; if (event.preventDefault) { event.preventDefault(); } else { event.returnValue = false; } } });
        _this.editbox.mousedown = false;
        _this.editbox.isCanSave = false;
        addEvent(_this.editbox, 'mousedown.edit', function() { _this.editbox.mousedown = true; });
        addEvent(_this.editbox, 'mouseup.edit', function() {
            if (isFirefox && _this.editbox.mousedown) { _this.saveRange(); }
            _this.editbox.mousedown = false;
        });
        addEvent(_this.editbox, 'mouseleave.edit', function() { if (_this.editbox.mousedown) { _this.editbox.isCanSave = true; } else { _this.editbox.isCanSave = false; } });
        addEvent(document, 'mouseup.edit', function() {
            if (_this.editbox.isCanSave) { _this.saveRange(); }
            _this.editbox.mousedown = false;
            _this.editbox.isCanSave = false;
        });
    }
    var setData = function(_ele, data) { _ele.easyData = data; return _ele; }
    var cloneNode = function(node) {
        var newNode = node.cloneNode(true);
        var newNodeEmoji = newNode.getElementsByTagName('img');
        var nodeEmoji = node.getElementsByTagName('img');
        var newNodeInput = newNode.getElementsByTagName('input');
        var nodeInput = node.getElementsByTagName('input');
        for (var i = 0; i < nodeEmoji.length; i++) { var data = JSON.parse(JSON.stringify(nodeEmoji[i].easyData));
            setData(newNodeEmoji[i], data); }
        for (var i = 0; i < nodeInput.length; i++) { var data = JSON.parse(JSON.stringify(nodeInput[i].easyData));
            setData(newNodeInput[i], data); }
        return newNode;
    }
    var getTextImage = function(color, text, width, fontSize, fontFamily) { var canvas = document.createElement('canvas');
        canvas.width = width;
        canvas.height = parseInt(fontSize); var ctx = canvas.getContext('2d');
        ctx.save();
        ctx.font = parseInt(fontSize) + 'px ' + fontFamily;
        ctx.fillStyle = color;
        ctx.textAlign = 'center';
        ctx.textBaseline = 'middle';
        ctx.fillText(text, canvas.width / 2, canvas.height / 2);
        ctx.restore(); return canvas.toDataURL('image/png'); }
    var EasyEditor = function(id) {
        this.editbox = document.getElementById(id);
        this.editbox.spellcheck = false;
        this.editbox.contentEditable = 'true';
        addClass(this.editbox, 'easyEditor');
        filter.call(this);
        bindEvent.call(this);
        restoreContent(this.editbox);
        var editboxStyle = getComputedStyle(this.editbox);
        this.fontFamily = editboxStyle['font-family'];
        this.fontSize = editboxStyle['font-size'];
        this.fontColor = editboxStyle['color'];
        this.focus = function() { this.editbox.focus();
            this.saveRange(); return this; };
        this.blur = function() { this.editbox.blur(); return this; };
        this.setPosition = function(position) {
            if (this.range == null) { this.focus(); } else if (position == 'start' || position == 'end') {
                var firstChild = this.editbox.firstChild;
                if (firstChild == null) { this.blur().focus(); } else {
                    var range = getRangeObject();
                    if (position == 'start') { range.setStartBefore(firstChild);
                        range.setEndBefore(firstChild); } else if (position == 'end') { range.setStartAfter(this.editbox.lastChild);
                        range.setEndAfter(this.editbox.lastChild); }
                    userSelection.removeAllRanges();
                    userSelection.addRange(range);
                    this.saveRange();
                }
            } else { console.error('[EasyEditor] position is not defined'); }
            return this;
        };
        this.selectAll = function() {
            var firstChild = this.editbox.firstChild;
            if (firstChild != null && this.range != null) { var range = getRangeObject();
                range.setStartBefore(firstChild);
                range.setEndAfter(this.editbox.lastChild);
                userSelection.removeAllRanges();
                userSelection.addRange(range);
                this.saveRange(); } else { this.focus(); }
            return this;
        };
        this.clearAll = function() { this.selectAll().clearSelect(); return this; };
        this.clearSelect = function() {
            if (this.range != null) { this.range.deleteContents();
                this.restoreSaveRange();
                restoreContent(this.editbox); } else { this.focus(); }
            return this;
        };
        this.changeLine = function() {
            if (!isChrome) { this.insertHTML('<br>'); } else { this.insertHTML('<br>&nbsp;'); var range = getRangeObject();
                range.setStart(range.startContainer, range.startOffset - 1);
                userSelection.removeAllRanges();
                userSelection.addRange(range);
                document.execCommand("Delete", false, null); }
            return this;
        };
        this.placeholder = function(str) { this.placeholderContent = true;
            this.placeholderText = str || '';
            checkPlaceholder.call(this); return this; };
        this.closePlaceholder = function() { this.placeholderContent = false;
            this.placeholderText = '';
            checkPlaceholder.call(this); return this; };
        this.insertEmoji = function(opts) {
            if (opts.src == undefined) { console.error('[EasyEditor] emoji src is not define'); return false; }
            if (!opts.remark) opts.remark = '';
            this.insertHTML('<img id="easy-editor-save" class="easy-emoji" src="' + opts.src + '" contenteditable="false"/>');
            var save = document.getElementById('easy-editor-save');
            setData(save, { saveValue: opts.remark, type: 'emoji', info: opts.data || '' }).removeAttribute('id');
            if (opts.afterInsert) { opts.afterInsert.call(this); }
            return this;
        };
        this.insertBlock = function(opts) {
            this.insertHTML('<br id="changeLinear"/><span id="easyEditorSaveWidth">' + opts.text + '</span>');
            var spanObj = document.getElementById('easyEditorSaveWidth');
            var width = getRect(spanObj).width;
            removeElement(spanObj);
            removeElement(document.getElementById('changeLinear'));
            var blockUrl = getTextImage(opts.color || this.fontColor, opts.text || '', width, this.fontSize, this.fontFamily);
            this.insertHTML('<img id="easy-editor-save" class="easy-block" src="' + blockUrl + '" contenteditable="false"/>');
            var save = document.getElementById('easy-editor-save');
            setData(save, { saveValue: opts.text, type: 'text', info: opts.data || '' }).removeAttribute('id');
            if (opts.afterInsert) { opts.afterInsert.call(this); }
            return this;
        };
        this.getContent = function(opts) {
            var emojiSign = opts.emojiSign || ['|', '|'];
            var blockSign = opts.blockSign || ['|', '|'];
            if (typeof emojiSign == 'string') { var emojiArr = [emojiSign, emojiSign];
                emojiSign = emojiArr; }
            if (typeof blockSign == 'string') { var blockArr = [blockSign, blockSign];
                blockSign = blockArr; }
            var editbox = cloneNode(this.editbox);
            var imgList = editbox.getElementsByTagName('img');
            var divList = editbox.getElementsByTagName('div');
            var pList = editbox.getElementsByTagName('p');
            var allData = [];
            var emojiData = [];
            var blockData = [];
            for (var i = 0; i < imgList.length; i++) {
                var oldNode = imgList[i],
                    data = oldNode.easyData,
                    sign;
                allData.push(data.info);
                if (data.type === 'emoji') { emojiData.push(data.info);
                    sign = emojiSign; } else if (data.type === 'text') { blockData.push(data.info);
                    sign = blockSign; }
                var newNode = document.createTextNode(sign[0] + data.saveValue + sign[1]);
                var parentNode = oldNode.parentNode;
                insertAfter(newNode, oldNode);
            }
            for (var i = 0; i < divList.length; i++) { if (i != divList.length - 1) { var oldNode = divList[i]; var newNode = document.createElement('br');
                    insertAfter(newNode, oldNode); } else if (divList[i].lastChild != null && divList[i].lastChild.tagName === 'BR') { removeElement(divList[i].lastChild); } }
            for (var i = 0; i < pList.length; i++) { if (i != pList.length - 1) { var oldNode = pList[i]; var newNode = document.createElement('br');
                    insertAfter(newNode, oldNode); } else if (pList[i].lastChild != null && pList[i].lastChild.tagName === 'BR') { removeElement(pList[i].lastChild); } }
            var html = editbox.innerHTML;
            return { text: html.replace(/<(?!\/?BR)[^<>]*>/gi, ''), data: allData, emojiData: emojiData, blockData: blockData }
        };
    }
    EasyEditor.prototype = {
        placeholderText: '',
        placeholderContent: false,
        range: null,
        getSelection: function() { return userSelection; },
        getRangeObject: function() { return getRangeObject(); },
        saveRange: function() { var range = getRangeObject();
            this.range = range; return this; },
        insertHTML: function(html) {
            if (this.range === null) { this.focus(); }
            var range = this.range;
            var oFragment = range.createContextualFragment(html);
            var oLastNode = oFragment.lastChild;
            range.deleteContents();
            range.insertNode(oFragment);
            range.setStartAfter(oLastNode);
            range.setEndAfter(oLastNode);
            userSelection.removeAllRanges();
            userSelection.addRange(range);
            this.saveRange();
            return this;
        },
        restoreSaveRange: function() {
            var range = this.range;
            if (range == null) { console.error('[EasyEditor] range is empty'); } else { setRange(range); }
            return this;
        },
    }
    window.easyEditor = function(id) {
        if (id == undefined || null) { console.error('[EasyEditor] editor id is not defined'); return; }
        return new EasyEditor(id);
    }
})();