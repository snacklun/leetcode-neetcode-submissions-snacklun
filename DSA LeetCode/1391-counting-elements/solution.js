/**
 * @param {number[]} arr
 * @return {number}
 */
var countElements = function(arr) {
    const set = new Set(arr);
    let cnt = 0;
    for (n of arr) {
        if (set.has(n+1)) {
            cnt++;
        }
    }
    return cnt;
};
