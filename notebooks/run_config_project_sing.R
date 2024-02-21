### get project script
FD_REPO = "/mount/repo"
FD_PRJ  = file.path(FD_REPO, "Proj_CombEffect_ENCODE_FCC")
FD_EXE  = file.path(FD_PRJ,  "scripts")

### source
fdiry = file.path(FD_EXE, "config_project_sing.R")
source(fdiry)