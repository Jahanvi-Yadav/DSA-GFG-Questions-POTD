//WAP OF WORD SEARCH
// THIS IS A GFG - POTD QUESTION OF WORD SEARCH USING JAVA. 
class Solution 
{
    private boolean dfs(char mat[][], String word,int index, int x, int y)
    {
        if(index==word.length())
            return true;
        if( x<0 || y<0 || x>=mat.length || y>=mat[0].length || mat[x][y]!=word.charAt(index))
            return false;
        
        char ch= mat[x][y];
        mat[x][y]='#';
        
        int dx[]= {-1,0,0,1};
        int dy[] = {0,1,-1,0};
        
        for(int z=0;z<4;z++)
        {
            if(dfs(mat,word,index+1,x+dx[z], y+dy[z]))
                return true;
        }
        
        mat[x][y]=ch;
        return false;
    }
    
    public boolean isWordExist(char[][] mat, String word)
    {
        // Code here
        int n= mat.length;
        int m= mat[0].length;
        boolean ans=false;
        for(int x=0;x<n;x++)
        {
            for(int y=0;y<m;y++)
            {
                if(mat[x][y]== word.charAt(0))
                {
                    if(dfs(mat, word, 0, x,y))
                        return true;
                }
            }
        }
        
        return false;  
    }
}
