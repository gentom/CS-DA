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
