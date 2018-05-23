var HPage = {
    divId: '',
    preUrl: '',
    sufUrl: '',
    page: 1,
    total: 1,
    per_page: 10,
    len: 5,
    pages: 1,
    range: [],
    init: function (divId, preUrl, sufUrl, param) {
        this.divId = divId;
        this.preUrl = preUrl;
        this.sufUrl = sufUrl;
        this.page = param.page || this.page;
        this.total = param.total || this.total;
        this.per_page = param.per_page || this.per_page;
        this.len = param.len || this.len;
        this.pages = this.total % this.per_page == 0 ? parseInt(this.total / this.per_page) : parseInt(this.total / this.per_page) + 1;
        this.range = this.createRange(this.page, this.pages, this.len);
        this.show();
    },
    show: function () {
        var range = this.range;
        var preHtml = '';
        if (1 == range[0]) {
            preHtml = '<li class="disabled">'
                + '<span><span aria-hidden="true">&laquo;</span></span>'
                + '</li>';
        } else {
            preHtml = '<li>' +
                '<a href="javascript:HPage.showPre();" aria-label="Previous">' +
                '<span aria-hidden="true">&laquo;</span>' +
                '</a>' +
                '</li>';
        }
        var nextHtml = '';
        if (this.pages == range[range.length - 1]) {
            nextHtml = '<li class="disabled">'
                + '<span><span aria-hidden="true">&raquo;</span></span>'
                + '</li>';
        } else {
            nextHtml = '<li>' +
                '<a href="javascript:HPage.showNext();" aria-label="Next">' +
                '<span aria-hidden="true">&raquo;</span>' +
                '</a>' +
                '</li>';
        }

        var html = '';
        for (var i = 0; i < range.length; i++) {
            var active = '';
            if (range[i] == this.page) {
                html += '<li class="active"><span>' + range[i] + '</span></li>';
            } else {
                html += '<li><a href="' + this.preUrl + range[i] + this.sufUrl + '">' + range[i] + '</a></li>';
            }
        }

        var pageHtml = '<nav aria-label="Page navigation">'
            + '<ul class="pagination pagination-sm">'
            + preHtml + html + nextHtml + '</ul>'
            + '</nav>';
        $("#" + this.divId).html(pageHtml);
    },
    showPre: function () {
        var min = this.range[0]
        if (min > 1) {
            this.range.unshift(min - 1);
            this.range.pop();
            this.show();
        }
    },
    showNext: function () {
        var max = this.range[this.range.length - 1];
        if (this.pages > max) {
            this.range.shift();
            this.range.push(max + 1);
            this.show();
        }
    },
    createRange: function (page, pages, len) {
        var range = [];
        if (len >= pages) {
            for (var i = 1; i <= pages; i++) {
                range.push(i);
            }
        } else {
            var mid = len % 2 == 0 ? parseInt(len / 2) : parseInt(len / 2) + 1;
            if (page - mid <= 0) {
                for (var i = 1; i <= len; i++) {
                    range.push(i);
                }
            } else if (page + mid >= pages) {
                for (var i = len; i > 0; i--) {
                    range.push(pages - i + 1);
                }
            } else if (page - mid > 0 && page + mid < pages) {
                for (var i = mid; i > 0; i--) {
                    range.push(page - i + 1);
                }
                for (var i = 1; i <= (len - mid); i++) {
                    range.push(page + i);
                }
            }
        }
        return range;
    }

}

