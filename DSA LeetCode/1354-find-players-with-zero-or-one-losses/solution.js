/**
 * @param {number[][]} matches
 * @return {number[][]}
 */
var findWinners = function(matches) {
    const newMap = new Map();
    const winMap = [];
    const loseMap = [];
    
    for (const [a,b] of matches) {
        newMap.set(a, (newMap.get(a) > 0 ? newMap.get(a) : 0 ));
        newMap.set(b, (newMap.get(b) || 0 ) + 1 );
    }
    for (const [k,v] of newMap) {
        if (v === 0) {
            winMap.push(k);
        }
        if (v === 1) {
            loseMap.push(k);
        }
    }

    winMap.sort((a,b) => a-b);
    loseMap.sort((a,b) => a-b);
    
    return [winMap, loseMap]
};
