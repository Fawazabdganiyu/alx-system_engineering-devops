#!/usr/bin/env ruby

match = ARGV[0].match(/\[from:(.*?)\] \[to:(.*?)\] \[flags:(.*?)\]/)
if match
  sender = match[1]
  receiver = match[2]
  flags = match[3]
end

puts "#{sender},#{receiver},#{flags}"
