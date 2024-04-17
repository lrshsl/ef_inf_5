local function shell_sort(arr, len)
	local gap = len / 2
	while gap > 0 do
		for i = gap + 1, len do
			local temp = arr[i]
			local j = i
			while j > gap and arr[j - gap] > temp do
				arr[j] = arr[j - gap]
				j = j - gap
			end
			arr[j] = temp
		end
		gap = math.floor(gap / 2)
	end
end

local function main()
	local arr = {}
	for i = 1, N do
		arr[i] = math.random(0, MAX_ELEMENT)
	end
	shell_sort(arr, N)
	print(table.concat(arr, ", "))
end

N = 100
MAX_ELEMENT = 10000

main()
