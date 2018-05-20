defmodule Recursion do
  def print_multiple_times(n) when n <= 1 do
    IO.puts Enum.random(0..1000)
  end

  def print_multiple_times(n) do
    IO.puts Enum.random(0..1000)
    print_multiple_times(n - 1)
  end
end

Recursion.print_multiple_times(50)

IO.puts "....................."
for x <- 0..10, do: IO.puts Enum.random(0..1000)
