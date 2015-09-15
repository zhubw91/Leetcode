# @param {Integer[]} nums
# @return {Boolean}
def contains_duplicate(nums)
	dup_hash = Hash.new
	nums.each do |value|
		if dup_hash[value].nil?
			dup_hash[value] = 1
		else
			return true
		end
	end 
	return false
end