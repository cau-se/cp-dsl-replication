(require 'package)
(add-to-list 'package-archives '("melpa" . "https://melpa.org/packages/"))

(package-initialize)

(unless package-archive-contents
  (package-refresh-contents))
(unless (package-installed-p 'lsp-mode))
  (package-install 'lsp-mode)

(add-to-list 'auto-mode-alist '("\\.oconf\\'" . oceandsl-mode))

;;add your folder to "oceandsl-mode.el" here as: "~/example/folder" for "~/bin"
(add-to-list 'load-path "~/bin")
(load-library "oceandsl-mode")
(add-to-list 'auto-mode-alist '("\\.oconf\\'" . oceandsl-mode))

(with-eval-after-load 'lsp-mode
  (add-to-list 'lsp-language-id-configuration
               '(oceandsl-mode . "oceandsl"))
  (lsp-register-client
   (make-lsp-client :major-modes '(oceandsl-mode)
                    :server-id 'oceandsl-ls
                    :activation-fn (lsp-activate-on "oceandsl")
                    :new-connection (lsp-stdio-connection (list "java" "-jar" oceandsl-ls-jar)))))
(custom-set-variables
 ;; custom-set-variables was added by Custom.
 ;; If you edit it by hand, you could mess it up, so be careful.
 ;; Your init file should contain only one such instance.
 ;; If there is more than one, they won't work right.
 '(package-selected-packages '(lsp-mode)))
(custom-set-faces
 ;; custom-set-faces was added by Custom.
 ;; If you edit it by hand, you could mess it up, so be careful.
 ;; Your init file should contain only one such instance.
 ;; If there is more than one, they won't work right.
 )
