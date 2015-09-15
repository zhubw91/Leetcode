# @param {Integer[]} nums
# @param {Integer} k
# @return {Boolean}
def contains_nearby_duplicate(nums, k)
	dup_hash = Hash.new
	nums.each_with_index do |value, index|
		if dup_hash[value].nil?
			dup_hash[value] = index
		elsif index - dup_hash[value] <= k
			return true
		else
			dup_hash[value] = index
		end
	end 
	return false
end