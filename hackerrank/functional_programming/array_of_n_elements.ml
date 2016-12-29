let make_array n = 
  let rec gogo c number acc =
    if c==number then acc else gogo (c+1) number acc@[c]
  in
  gogo 0 n [];;


let () =
  let n = int_of_string (read_line ()) in
  let arr = make_array n in
  List.iter ( Printf.printf "%d " ) arr