'''
GIT 구조

Repository = 형태적으로는 폴더. 의미적으로는 하나의 프로젝트에 해당된다. 
local repository = 로컬하게 저장된 repository
remote repository = Github에 저장된 repository

local-remote 간 오가면서 작업하는 것이 핵심이다. github에 저장된 remote repository를 pull해올 수도 있고, 
local repository를 github으로 옮기는 건 push라고 한다. 

[branch]
가장 기본으로 main branch가 있다. main branch가 프로젝트 진짜최종최종최종.doc 같은 버전이고, 여러가지 branch가 현재 작업 중인 파일들이다.
branch는 merge라는 작업을 통해서 main branch와 합쳐질 수 있다. 다시말해 merge를 하지 않으면 branch에서 이루어지는 변경점은 
main에 반영되지 않는다. 

branch에 올라가기 전에도 여러 단계가 있다. 
즉 working directory, 현재 작업 중인 디렉토리에서 add 작업을 통해 staging area로 옮기고, 
stating area에서 commit을 해야 localrepo로 옮겨가고, 

localrepo에서 최종적으로 remote repository로 push (sync를 하면 push가 이루어짐) 를 해야 github에 최종본이 등재된다. 

그리고 Explorer에서 보이는 파일은 현재 컴퓨터에 로컬하게 저장된 파일이기도 하지만, 
일단 repository를 연동해놓은 이상 remote repository와 현재 로컬에 있는 폴더의 내용물들은 push and pull하는 과정에서 자동으로 sync된다.
'''