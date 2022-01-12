let rec fibonacci n =
  if n < 3 then 1
  else (fibonacci (n-1)) + (fibonacci (n-2))

let map n f s =
  if n == 1 then List.map f s
  else failwith "impossible"

let rand_range min max =
  min + Random.int (max - min)

