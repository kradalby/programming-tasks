let rec read_lines () =
  try let line = read_line () in
    int_of_string (line) :: read_lines()
  with
    End_of_file -> []

let f lst = 
  let rec aux acc  = function
    | [] -> acc;
    | h::t -> 
      match (h mod 2) with
      | 0 -> aux acc t
      | _ -> aux (acc+h) t
  in 
  aux 0 lst

let () = 
  let arr = read_lines() in
  let ans = f arr in
  print_int ans;;