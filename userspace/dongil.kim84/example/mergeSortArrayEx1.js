//using jsfiddle(https://jsfiddle.net)
//divide and conquer

var exampleArr = new Array(8,6,14,18,12,20,10,4,16,2);
alert(mergeSortArray(exampleArr));

function mergeSortArray(arr){

  if(arr.length <2)
    return arr;

	var mid = Math.floor(arr.length/2),
      left = arr.slice(0,mid),
      right = arr.slice(mid);

  return mergeSort(mergeSortArray(left),mergeSortArray(right));
}

function mergeSort(left, right){
  var result = [], l = 0, r = 0;
  
  while(l < left.length && r < right.length){
    if(left[l] < right[r])
      result.push(left[l++]);
    else
      result.push(right[r++]);
  }  

  return result.concat(left.slice(l)).concat(right.slice(r));
}
