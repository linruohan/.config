
class EasyWrapError < StandardError;end
class NotValidElementError < EasyWrapError;end
class IncorrectdIndexError < EasyWrapError;end

class TableBase
    attr_reader :e
    def initialize e
        raise NotValidElementError unless e.is_a?(Selenium::WebDriver::Element)
        @e = e
    end

    def method_missing(m, *params, &blk)
        @e.send(m, *params) if @e.respond_to?(m)
    end
end #TableBase
class Table < TableBase
    def initialize e
        super(e)
        __rows
    end
    def __rows
        @rows = @e.find_elements(:css => 'tr')
    end
    private :__rows

    def rows
        all_rows = []
        @rows.each { r rows << TableRow.new(r)}
        all_rows
    end

    def row_count
        @rows.size
    end

    def [](index)
        valid_index? index
        TableRow.new @rows[index]
    end

    def valid_index?(index)
        raise IncorrectdIndexError if index.to_i > row_count
    end
end #Table

class TableRow < TableBase
    def initialize e
        super(e)
        __cells
    end

    def __cells
        @cells = @e.find_elements(:tag_name => 'td')
        # 如果找不到td那么试着去找th
        @cells = @e.find_elements(:tag_name => 'th') if @cells.empty?
    end
    private :__cells

    def cells
        all_cells = []
        @cells.each {c all_cells << TableCell.new(c)}
    end

    def cell_count
        @cells.size
    end

    def [](index)
        valid_index? index
        TableCell.new @cells[index]
    end

    def valid_index?(index)
        raise IncorrectdIndexError if index.to_i > cell_count
    end
end #TableRow

class TableCell < TableBase
end #TableCell
end #EasyWrap
