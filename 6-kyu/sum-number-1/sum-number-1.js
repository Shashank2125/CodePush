function sum(x) {
  let total=x??0;
  function inner(y){
    if(y===undefined){
      return total;
    }
    total+=y;
    return inner;
  }
  return x===undefined?total :inner
}