# @param {Integer} a
# @param {Integer} b
# @param {Integer} c
# @param {Integer} d
# @param {Integer} e
# @param {Integer} f
# @param {Integer} g
# @param {Integer} h
# @return {Integer}
def compute_area(a, b, c, d, e, f, g, h)
	if e < c and g > a and h > b and d > f 
		area =  ([c,g].min - [e,a].max)*([d,h].min - [b,f].max)
	else
		area = 0
	end 

	return (d - b)*(c - a) + (h - f)*(g - e) - area
end