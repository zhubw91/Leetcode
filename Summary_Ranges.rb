# @param {Integer[]} nums
# @return {String[]}
def summary_ranges(nums)
    result = []
    return result if nums.empty?
    top = nums[0]
    tail = top
    nums.each_with_index do |value, index|
        next if index == 0
        if value == tail + 1
            tail = value
        elsif tail == top
            result.push "#{top}"
            top = value
            tail = value
        else
            result.push "#{top}->#{tail}"
            top = value
            tail = value
        end     
    end
    # check the last range
    if top == tail
        result.push "#{top}"
    else
        result.push "#{top}->#{tail}"
    end
    return result
end

puts summary_ranges([])