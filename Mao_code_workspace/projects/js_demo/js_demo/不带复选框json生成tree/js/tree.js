var selectData;
$("#modalDialog").draggable({ cursor: "move", handle: '.modal-header' });

function loadTree(tData) {
    var ul = $('<ul>');
    for (var i = 0; i < tData.length; i++) {
        var li = $('<li>').appendTo(ul);
        var node = $('<a>').appendTo(li);
        var icon = $('<i>').css('margin-right', '5').appendTo(node);
        var aTree = $('<span>').html(tData[i].title).appendTo(node);
        var input = $('<input>').addClass('field').val(tData[i].field).css({ 'display': 'none' }).appendTo(node);
        if (tData[i].children != undefined) {
            icon.addClass(tData[i].open ? 'fa fa-minus-square-o' : 'fa fa-plus-square-o');
            var ic = $('<i>').addClass('fa fa-folder-open-o');
            icon.after(ic).addClass('status');
            node.addClass('tree-node');
            $('<input>').addClass('open').val(tData[i].open).css('display', 'none').appendTo(node);
            var $child = loadTree(tData[i].children);
            if (tData[i].open) { $child.show().appendTo(li); } else { $child.hide().appendTo(li); }
        } else {
            icon.addClass('fa fa-file-text-o');
            $('<input>').addClass('candidate').val(tData[i].candidate).css('display', 'none').appendTo(li);
        }
    }
    return ul;
}

function nodeClick(box) {
    box.find('.tree-node').click(function() {
        if ($.trim($(this).find('.open').val()) == 'true') {
            $(this).next().slideUp(500);
            $(this).find('.open').val('false');
            $(this).find('.status').removeClass('fa-minus-square-o').addClass('fa-plus-square-o');
        } else {
            $(this).next().find('.tree-node').each(function() {
                $(this).next().css('display', 'none');
                $(this).find('.open').val('false');
                $(this).find('.status').removeClass('fa-minus-square-o').addClass('fa-plus-square-o');
            })
            $(this).find('.open').val('true');
            $(this).find('.status').removeClass('fa-plus-square-o').addClass('fa-minus-square-o');
            $(this).next().slideDown(500);
        }
    })
}

function loadTreeTable(tData) {
    var outCol = tData.length;
    var treeTable = $('<table cellspacing="0" cellpadding="0" border="1">').css('border-collapse', 'collapse').addClass('tree-table');
    var trTitle = $('<tr>').addClass('tr-title').appendTo(treeTable);
    var trContent = $('<tr>').addClass('tr-content').appendTo(treeTable);
    for (var i = 0; i < tData.length; i++) {
        var childTable = undefined;
        if (tData[i].children != undefined && tData[i].children.length > 0) {
            childTable = loadTreeTable(tData[i].children);
            childTable.css({ 'border-width': '0px', 'border-style': 'hidden' })
            var childTrTitle = childTable.find('.tr-title').first();
            $('<td>').addClass('td-title').attr('colspan', tData[i].children.length).html(tData[i].title).appendTo(childTrTitle);
            $('<td>').addClass('t-node-table').html(childTable).appendTo(trContent);
        } else {
            var td = $('<td>').appendTo(trContent);
            $('<span>').html(tData[i].title).appendTo(td);
            if (tData[i].candidate != undefined && (tData[i].candidate == false || tData[i].candidate == 'false')) { td.addClass('t-select t-default'); }
            $('<input>').addClass('candidate').css('display', 'none').val(tData[i].candidate).appendTo(td);
            $('<input>').addClass('field').css('display', 'none').val(tData[i].field).appendTo(td);
            td.addClass('t-leaf');
        }
    }
    return treeTable;
}

function cancelSelect(td) {
    var isAllSelect = true;
    td.parent().find('.t-leaf').each(function() { if ($(this).find('.candidate').val() == false || $.trim($(this).find('.candidate').val()) == 'false') { isAllSelect = false; return isAllSelect; } })
    var trTitle = td.parent().prev();
    var parentTd = trTitle.parent().parent();
    if (isAllSelect != false) {
        trTitle.find('.td-title').removeClass('t-select');
        cancelSelect(parentTd);
    }
}

function packDataNode(table) {
    var parentData;
    var childData = [];
    var titleContent = table.find('.tr-title').first().children('.t-select').html();
    table.find('.tr-content').first().children('.t-select').each(function() { childData.push({ title: $.trim($(this).find('span').html()), field: $(this).find('.field').val(), candidate: $(this).hasClass('t-default') ? false : true }); })
    table.find('.tr-content').first().children('.t-node-table').each(function() { if ($(this).find('table').first().find('.td-title').first().hasClass('t-select')) { childData.push(packDataNode($(this).find('table').first())); } })
    if (titleContent != undefined && $.trim(titleContent) != '' && childData.length > 0) { parentData = { title: titleContent, open: true, children: childData }; } else { return childData; }
    return parentData;
}

function tableClick() {
    var newData = [{ title: '编码', field: "code", candidate: false }];
    $('.t-leaf').click(function() {
        if ($.trim($(this).find('.candidate').val()) == 'true' || $(this).find('.candidate').val() == true) {
            $(this).addClass('t-select');
            $(this).find('.candidate').val('false');
            $(this).parents('.tr-content').prev().find('.td-title').addClass('t-select');
        } else {
            $(this).removeClass('t-select');
            $(this).find('.candidate').val('true');
            cancelSelect($(this));
        }
        $('#select_tree_table').empty();
        selectData = packDataNode($('#tree_table>.tree-table'));
        $('#select_tree_table').append(loadTreeTable(selectData));
    })
    $('.td-title').click(function() {
        var isAllSelect = true;
        $(this).parent().next().find('.t-leaf').each(function() { if ($.trim($(this).find('.candidate').val()) == 'true') { isAllSelect = false; return isAllSelect; } })
        if (isAllSelect == false) {
            $(this).parent().parent().find('.t-leaf,.td-title').addClass('t-select');
            $(this).parent().parent().find('.t-leaf').each(function() { $(this).find('.candidate').val('false'); })
            $(this).parents('.tr-content').prev().find('.td-title').addClass('t-select');
        } else {
            $(this).parent().parent().find('.t-leaf,.td-title').removeClass('t-select');
            $(this).parent().parent().find('.t-leaf').each(function() { $(this).find('.candidate').val('true'); })
            cancelSelect($(this).parent().parent().parent());
        }
        $('#select_tree_table').empty();
        selectData = packDataNode($('#tree_table>.tree-table'));
        $('#select_tree_table').append(loadTreeTable(selectData));
    })
}

function result(selData) {
    var datas = new Array();
    for (var i = 0; i < selData.length; i++) { if (selData[i].children != undefined && selData[i].children.length > 0) { var child = result(selData[i].children); for (var j = 0; j < child.length; j++) { datas.push(child[j]); } } else { if (selData[i].field != 'code') { datas.push('\"' + selData[i].field + '\"'); } } }
    return datas;
}