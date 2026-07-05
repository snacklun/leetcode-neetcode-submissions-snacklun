/**
 * @param {string} sentence
 * @return {boolean}
 */
var checkIfPangram = function(sentence) {
    const set = new Set();
    for (const s of sentence) {
        set.add(s);
    }
    console.log(set.size)
    return set.size === 26 ? true : false;
};
