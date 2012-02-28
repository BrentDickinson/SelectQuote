import sublime, sublime_plugin
import re

class selectquoteCommand(sublime_plugin.TextCommand):
    counter = 0

    def createStop(self,match):
        self.counter = self.counter + 1
        return(match.group(1) + '${'+str(self.counter)+':' + match.group(2) + '}' + match.group(1))

    def run(self, edit):
        for region in self.view.sel():
                line = self.view.line(region)
                line_contents = self.view.substr(line)
                lregion = sublime.Region(line.a,line.b)

                contents = line_contents.replace("$","\$");
                contents=re.sub("([\"'])(.+?)\\1",self.createStop,contents,re.M)
                self.view.sel().clear()
                self.view.sel().add(lregion)

                self.view.run_command('insert_snippet', {'contents': contents})
                self.counter=0;