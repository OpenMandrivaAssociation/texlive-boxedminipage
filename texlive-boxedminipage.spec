%global tl_name boxedminipage
%global tl_revision 77682

Name:		texlive-%{tl_name}
Epoch:		1
Version:	1.1
Release:	%{tl_revision}.1
Summary:	Framed minipages of a specified total width (text and frame combined)
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/boxedminipage
License:	lppl1.3c
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/boxedminipage.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/boxedminipage.doc.r%{tl_revision}.tar.xz
Source2:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/boxedminipage.source.r%{tl_revision}.tar.xz
BuildArch:	noarch
Requires(pre):	texlive-tlpkg
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
The package essentially just wraps a minipage within an \fbox. However,
while \fbox{\begin{minipage}{\linewidth}...\end{minipage}} juts out into
the margin, \begin{boxedminipage}...\end{boxedminipage} does not.
Instead, it subtracts the frame's dimensions from the specified
dimensions of the minipage before typesetting the minipage. Note: The
package was formerly known as boxedminipage2e and now replaces Mario
Wolczko's earlier boxedminipage package.

%prep
%setup -q -c -a1 -a2
rm -rf tlpkg
if [ -d RELOC ]; then
	cp -a RELOC/. .
	rm -rf RELOC
fi

%build

%install
mkdir -p %{buildroot}%{_datadir}/texmf-dist
# Flat tlnet layout: tex/ doc/ source/ fonts/ ... -> texmf-dist/
if [ -d texmf-dist ]; then
	cp -a texmf-dist/. %{buildroot}%{_datadir}/texmf-dist/
elif [ -d texmf ]; then
	mkdir -p %{buildroot}%{_datadir}/texmf
	cp -a texmf/. %{buildroot}%{_datadir}/texmf/
else
	for d in * .[!.]* ..?*; do
		[ -e "$d" ] || continue
		case "$d" in tlpkg|RELOC) continue ;; esac
		cp -a "$d" %{buildroot}%{_datadir}/texmf-dist/
	done
fi
rm -rf %{buildroot}%{_datadir}/texmf-dist/tlpkg

%files
%dir %{_datadir}/texmf-dist
%dir %{_datadir}/texmf-dist/doc
%dir %{_datadir}/texmf-dist/source
%dir %{_datadir}/texmf-dist/tex
%dir %{_datadir}/texmf-dist/doc/latex
%dir %{_datadir}/texmf-dist/source/latex
%dir %{_datadir}/texmf-dist/tex/latex
%dir %{_datadir}/texmf-dist/doc/latex/boxedminipage
%dir %{_datadir}/texmf-dist/source/latex/boxedminipage
%dir %{_datadir}/texmf-dist/tex/latex/boxedminipage
%doc %{_datadir}/texmf-dist/doc/latex/boxedminipage/README
%doc %{_datadir}/texmf-dist/doc/latex/boxedminipage/boxedminipage.pdf
%doc %{_datadir}/texmf-dist/source/latex/boxedminipage/boxedminipage.dtx
%doc %{_datadir}/texmf-dist/source/latex/boxedminipage/boxedminipage.ins
%{_datadir}/texmf-dist/tex/latex/boxedminipage/boxedminipage.sty
%{_datadir}/texmf-dist/tex/latex/boxedminipage/boxedminipage2e.sty
