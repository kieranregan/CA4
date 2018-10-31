from process_changes_with_object import Commit

FileProcesser = Commit("Revision","Author","Date","Time","NoOfLines")

Data = FileProcesser.read_file("changes_python.txt")

Commits = FileProcesser.get_commits(Data)

FileProcesser.save_commits(Commits, "output.csv")



