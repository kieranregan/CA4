from process_changes import Processer

FileProcesser = Processer()

Data = FileProcesser.read_file("changes_python.log.txt")

Commits = FileProcesser.getCommits(Data)

FileProcesser.save_commits(Data, "output.csv")



