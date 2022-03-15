/**
 * @param {number} n
 * @param {number[][]} trust
 * @return {number}
 */
 var findJudge = function(n, trust) {
    if(trust.length==1) return trust[0][1]
    // // console.log(trust.length)
    // for(let i=0;i<trust.length;i++){
    //     console.log(trust[i])
    // }
    let people={}
    for(let i=1;i<=n;i++){
        people[i]=0
    }
    for(let i=1;i<=n;i++){
        for(let j=0;j<trust.length;j++){
                if(i!==trust[j][0] && i===trust[j][1]){
                people[i]=people[i]+1
            }else{
                if(i!==trust[j][0] && i!==trust[j][1]){
                    continue
                }
                people[i]=0

            }
        }
    }
    for(let i=1;i<=n;i++){
        if(people[i]===n-1){
            return i
        }
    }
    return -1
};

console.log({
    res:
findJudge(
4,
// [[1,3],[2,3],[3,1]]
[[1,3],[1,4],[2,3],[2,4],[4,3]]
)
})