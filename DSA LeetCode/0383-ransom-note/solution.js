/**
 * @param {string} ransomNote
 * @param {string} magazine
 * @return {boolean}
 */
var canConstruct = function(ransomNote, magazine) {
    let newMap = new Map();
    for (const key of magazine) {
        newMap.set(key, (newMap.get(key) || 0) + 1 );
    }
    // console.log('-----');
    // console.log(newMap);
    
    for (const ran of ransomNote) {
        const value = newMap.get(ran);
            // console.log('-----');
            // console.log(ran);
            // console.log(value);

        if (!value || value === 0 ) return false;
        
        if (value > 0) {
            newMap.set(ran,  value - 1);
        }
    }
    return true;
};
