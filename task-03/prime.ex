defmodule PrimeNumbers do
  def is_prime(num) when num <= 1, do: false
  def is_prime(num) do
    Enum.all?(2..trunc(:math.sqrt(num)), fn i -> rem(num, i) != 0 end)
  end
end

IO.puts("Enter a number: ")
n = String.to_integer(IO.gets(""))

IO.puts("Prime numbers up to #{n} are:")
for i <- 2..n do
  if PrimeNumbers.is_prime(i) do
    IO.write("#{i} ")
  end
end
