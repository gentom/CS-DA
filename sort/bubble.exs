defmodule Bubble do
  def sort(list) when is_list(list) do
    t = sort_move(list)

    if t == list do t else sort(t) end
  end

  def sort_move([x, y | t]) when x > y, do: [y | sort_move([x | t])]
  def sort_move([x, y | t]), do: [x | sort_move([y | t])]
  def sort_move(list), do: list
end

defmodule RNAGen do
  def random_int_array(length, list \\ [])
  def random_int_array(0, list), do: list
  def random_int_array(length, list) do
    length - 1
    |> random_int_array([random_int_num() | list])
  end

  defp random_int_num() do
    Enum.random(0..100)
  end
end

rlist = RNAGen.random_int_array(20)
IO.inspect rlist
IO.inspect Bubble.sort(rlist)
