-- Read in the input file an create a table from the rows in the text document
local inputPath = arg[1]

---- v Helper Functions v ----

-- Check that the file exists, returns true or false
local function file_exists(file)
  local f = io.open(file, "rb")
  if f then
    f:close()
  end
  return f ~= nil
end

local function lines_from(file)
  -- If the file does not exist, return an empty table
  if not file_exists(file) then
    return {}
  end

  local lines = {}
  -- Read the lines from the file
  for line in io.lines(file) do
    lines[#lines + 1] = line
  end

  return lines
end

---- ^ Helper Functions ^ ----

local input = lines_from(inputPath)
local num_of_increases = 0

-- Loop through and compare each lines to the previous line.
-- If the current line is higher than the previous line then the
-- depth has incresed.
for i, v in ipairs(input) do
  if i > 1 then
    if v > input[i - 1] then
      num_of_increases = num_of_increases + 1
    end
  end
end

-- Print out the number of times the value increased
print(num_of_increases)

-- The correct answer is 1195 but I am getting an output of 1194.
-- TODO: Come back and figure out this off by one error
