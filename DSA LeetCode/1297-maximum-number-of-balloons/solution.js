/**
 * @param {string} text
 * @return {number}
 */
var maxNumberOfBalloons = function(text) {
    let bCnt = 0;
    let aCnt = 0;
    let lCnt = 0;
    let oCnt = 0;
    let nCnt = 0;

    for (const t of text) {
        if (t === 'b') bCnt++;
        if (t === 'a') aCnt++;
        if (t === 'l') lCnt++;
        if (t === 'o') oCnt++;
        if (t === 'n') nCnt++;
    }
    if (bCnt === 0 || aCnt ===0 || lCnt < 2 || oCnt < 2 || nCnt === 0) {
        return 0;
    }
    lCnt = parseInt(lCnt/2);
    oCnt = parseInt(oCnt/2);
    return Math.min(bCnt, Math.min(aCnt, Math.min(lCnt, Math.min(oCnt, nCnt))));
};
