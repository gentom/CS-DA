'''
defmodule Selection do
  def sort(list) when is_list(list) do
    do_selection(list, [])
  end

  def do_selection([head|[]], acc) do
    acc ++ [head]
  end
  def do_selection(list, acc) do
    min = min(list)
    do_selection(:lists.delete(min, list), acc ++ [min])
  end

  defp min([first|[second|[]]]) do
    smaller(first, second)
  end
  defp min([first|[second|tail]]) do
    min([smaller(first, second)|tail])
  end

  defp smaller(e1, e2) do
    if e1 <= e2 do e1 else e2 end
  end
end
'''
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

defmodule Selection do
	def sort([]), do: []

	def sort(list), do: sort(list, [])

	defp sort([], sorted), do: sorted

	defp sort(unsorted, sorted) do
		maxx = select_max(unsorted, [])
		reduced_unsorted = List.delete(unsorted, maxx)

		sort(reduced_unsorted, [maxx | sorted])
	end

	defp select_max([], [maxx]), do: maxx

	defp select_max([h | t], []),
		do: select_max(t, [h])

	defp select_max([h | t], [maxx]) do
		if (h > maxx),
			do: select_max(t, [h]),
			else: select_max(t, [maxx])
	end

end


rlist = RNAGen.random_int_array(20)
IO.inspect rlist
IO.inspect Selection.sort(rlist)

